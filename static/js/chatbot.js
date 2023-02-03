var responses = {
  "did not arrive": " You can either contact the seller directly to resolve the issue or message our customer support staff",
  "broken": "I'm just a chatbot, I don't have feelings. How can I help you?",
  "what's your name": "My name is Chatbot. Nice to meet you.",
  "default": "I'm sorry, I didn't understand your question."
};

lst_responses = []
for (const [key, value] of Object.entries(responses)) {
  lst_responses.push(key)
}
console.log(lst_responses)

document.querySelector('#chatbot-submit').addEventListener('click', function(event) {
  event.preventDefault();
  var input = document.querySelector('#chatbot-input').value;
  document.querySelector('#chatbot-input').value = '';
  for (let key in responses) {
  console.log(key, input)
  console.log(input.includes(key))
    if (input.includes(key)) {
        var response = responses[key.toLowerCase()] || responses["default"];
        var messages = document.querySelector('#chatbot-messages');
        messages.innerHTML += '<div>' + response + '</div> <br>';
        break
    }
    else if (key == lst_responses[lst_responses.length - 1]) {
        var response = responses["default"];
        var messages = document.querySelector('#chatbot-messages');
        messages.innerHTML += '<div>' + response + '</div> <br>';
        break
    };
  };
});