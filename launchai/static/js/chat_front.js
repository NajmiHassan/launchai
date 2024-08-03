const sourceKnowledge = `
you are a learning assistant for students who want to make their startups by guiding them and give them what they want 
` ;

import { GoogleGenerativeAI } from "https://esm.run/@google/generative-ai";


const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");

let userMessage = null; // Variable to store user's message
const API_KEY = "sk-proj-Gz8uoyVCYi2NbeIqoX71T3BlbkFJGcWse1Bzza86P08kpIDP"; // Paste your API key here
const GOOGLE_API_KEY="AIzaSyCa0mvC9U89It-kGDjtfapHtXrNV-7GcMI" ;

const genAI = new GoogleGenerativeAI(GOOGLE_API_KEY);


function promptTemplate(query) {
    // Feed into an augmented prompt
    const augmentedPrompt = `
    contest :${sourceKnowledge}
    Query: ${query}`;
    
    return augmentedPrompt;
}

async function run(prompt) {
    const response = await fetch('http://localhost:8000/learning_chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_prompt: prompt,
        }),
    });
    
    const data = await response.json();
    console.log(data.message)
    return data.message;
  }

const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    // Create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<img src="/static/images/icons/chatbot.svg" class="bot-img" alt="esi bot" width="48" height="48"><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; // return chat <li> element
}


// Access your API key (see "Set up your API key" above)


const handleChat = () => {
    userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
    if(!userMessage) return;

    // Clear the input textarea and set its height to default
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    // Append the user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        // Display "Thinking..." message while waiting for the response
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        //const result =  gemini_model.generateContent(prompt);

        const messageElement = incomingChatLi.querySelector("p");
 
        console.log(userMessage)
        const my_prompt = promptTemplate(userMessage)
        //generateResponse(incomingChatLi);
        run(my_prompt).then(text => {
            messageElement.textContent = text;
            console.log(text);  // This will log the text returned from the run function
            }).catch(() => {
            messageElement.classList.add("error");
            messageElement.textContent = "Oops! Something went wrong. Please try again.";
            });

        //generateResponse(incomingChatLi);
    }, 600);
}

chatInput.addEventListener("input", () => {
    // Adjust the height of the input textarea based on its content
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window 
    // width is greater than 800px, handle the chat
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
document.body.classList.toggle("show-chatbot");
