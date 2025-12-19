import './App.css'
import Summary from './components/summary'
import { getStocks, getSummaries } from './services/api'
import { useEffect, useState } from 'react';


function App() {

  const [summaries, setSummaries] = useState([]);
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    async function loadData() {
      const summariesData = await getSummaries();
      const stocksData = await getStocks();

      setSummaries(summariesData);
      setStocks(stocksData);
    }

    loadData();
  }, []);


  return (
    <>
    <div className='header'>
      <h2>My Stock Tracker</h2>
    </div>
      <h1>Stock Summaries</h1>
      <div className='summary-list'>
        {summaries.map((summary, index) => (
          <Summary 
            key={index}
            company={summary.company} 
            ticker={summary.ticker} 
            title={summary.title} 
            body={summary.body} 
            sentiment={summary.sentiment} 
            key_points={summary.key_points}
            />
        ))}

      </div>
    </>
  )
}

export default App
