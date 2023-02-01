import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { TweetsComponent, TweetDetailComponent } from './tweets';
import reportWebVitals from './reportWebVitals';

const appEl = document.getElementById('root')
if (appEl){
  ReactDOM.render(<App />, appEl);
}

const e = React.createElement
const tweetsEl = document.getElementById('tweetme')
if (tweetsEl){
  const myComponent = e(TweetsComponent, tweetsEl.dataset)
  ReactDOM.render(myComponent, tweetsEl);
}

const tweetDetailElements = document.querySelectorAll(".tweetme-detail")
tweetDetailElements.forEach(container=>{
  ReactDOM.render( e(TweetDetailComponent, container.dataset), container);

})
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
