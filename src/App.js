import React, { Component } from 'react';
import { Widget, addResponseMessage, addLinkSnippet, addUserMessage, renderCustomComponent } from 'react-chat-widget';

import 'react-chat-widget/lib/styles.css';
import Reply from './components/Reply/Reply'

import './App.css'

import logo from './profile-bot.jpg';

class App extends Component {
  componentDidMount() {
    addResponseMessage("Hey! How may I help you?");
  }

  handleNewUserMessage = (newMessage) => {
    console.log(`New message incomig! ${newMessage}`);

    const data = {
      newMessage: newMessage,
    }

    fetch('http://18.234.161.91:8086/chat/', {
      method: 'post',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => {
        if (response.status !== 200) {
          console.log('Looks like there was a problem. Status Code: ' +
            response.status);
          return;
        }

        response.json().then((result) => {

          // addLinkSnippet({
          //   title: 'My awesome link',
          //   link: 'https://github.com/Wolox/react-chat-widget',
          //   target: '_blank'
          // })

          // renderCustomComponent(Reply)

          addResponseMessage(result.result.fulfillment.speech);
        })
      });

  }



  render() {
    return (
      <div className="App">
        <Widget
          handleNewUserMessage={this.handleNewUserMessage}
          profileAvatar={logo}
          title="HR smart bot"
          subtitle="Talk to me..!!"
          
        />
      </div>
    );
  }
}

export default App;