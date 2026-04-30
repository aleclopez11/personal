import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import axios from 'axios'


function App() {
  const [count, setCount] = useState(0)
  const [stock_data, getStockData] = useState({})

  useEffect(() => {
    console.log('useEffect called');
    const socket = new WebSocket('ws://127.0.0.1:8000/ws');
    console.log('WebSocket connection established');

    socket.onopen = () => {
      console.log('WebSocket connection opened');
    }
    socket.onmessage = (event) => {
      console.log('message received')
      const data = JSON.parse(event.data);
      console.log(data);
      if (data.length > 0) {
        getStockData(data);
      }
    }
    return () => {socket.close()};
  }, []);

  const sendMessae = () => {
    if (socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify({ message: 'Hello from React!' }));
    }
  }


  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
          <img src={reactLogo} className="framework" alt="React logo" />
          <img src={viteLogo} className="vite" alt="Vite logo" />
        </div>
        <div>
          <h1>Get started</h1>
          <p>
            Edit <code>src/App.jsx</code> and save to test <code>HMR</code>
          </p>
        </div>
        <button
          className="counter"
          // onClick={() => setCount((count) => count + 1)}
          onClick={() => axios.get('http://127.0.0.1:8000/stocks').then(
            (response) => {
              // const data = response.json();
            getStockData(response.data)
          })}
        >
          Count is {count}
        </button>
        <div>
          {/* <pre>Stock Data: {JSON.stringify(stock_data, null, 2)}</pre>           */}
        </div>
      </section>

      <div className="ticks"></div>

      <section id="next-steps">
        <div id="docs">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#documentation-icon"></use>
          </svg>
          <h2>Documentation</h2>
          <p>Your questions, answered</p>
          <ul>
            <li>
              <a href="https://vite.dev/" target="_blank">
                <img className="logo" src={viteLogo} alt="" />
                Explore Vite
              </a>
            </li>
            <li>
              <a href="https://react.dev/" target="_blank">
                <img className="button-icon" src={reactLogo} alt="" />
                Learn more
              </a>
            </li>
          </ul>
        </div>
        <div id="social">
          <svg className="icon" role="presentation" aria-hidden="true">
            <use href="/icons.svg#social-icon"></use>
          </svg>
          <h2>Connect with us</h2>
          <p>Join the Vite community</p>
          <ul>
            <li>
              <a href="https://github.com/vitejs/vite" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#github-icon"></use>
                </svg>
                GitHub
              </a>
            </li>
            <li>
              <a href="https://chat.vite.dev/" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#discord-icon"></use>
                </svg>
                Discord
              </a>
            </li>
            <li>
              <a href="https://x.com/vite_js" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#x-icon"></use>
                </svg>
                X.com
              </a>
            </li>
            <li>
              <a href="https://bsky.app/profile/vite.dev" target="_blank">
                <svg
                  className="button-icon"
                  role="presentation"
                  aria-hidden="true"
                >
                  <use href="/icons.svg#bluesky-icon"></use>
                </svg>
                Bluesky
              </a>
            </li>
          </ul>
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
      <h2>Stock Data</h2>
      <table>
    <thead>
      <tr>
        <th>Symbol</th>
        <th>Price</th>
        <th>open</th>
        <th>prev close</th>
        <th>change</th>
        <th>revenue (millions)</th>
        <th>profitMargins</th>
        <th>volume</th>


        {/* Add more columns as needed */}
      </tr>
    </thead>
    <tbody>
    {Object.entries(stock_data).map(([key, item]) => (
  console.log(key, item),
  <tr key={key}>
    <td>{key}</td>
    <td>{item.currentPrice}</td>
    <td>{item.open}</td>
    <td>{item.previousClose}</td>
    <td>{item.trend}%</td>
    <td>{(item.totalRevenue/ 1000000).toFixed(2)}</td>
    <td>{(item.profitMargins * 100).toFixed(2) + '%'}</td>
    <td>{item.volume.toLocaleString()}</td>
    {/* Add more cells as needed */}
  </tr>
))}
    </tbody>
  </table>
  <br />
  <section id="spacer"></section>
    </>
  )
}

export default App
