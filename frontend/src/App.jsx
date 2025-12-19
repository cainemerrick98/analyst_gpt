import './App.css'
import Summary from './components/summary'
import { getStocks, getSummaries } from './services/api'


function App() {

  const summaries = getSummaries()
  const stocks = getStocks()

  return (
    <>
    <div className='header'>
      <h2>My Stock Tracker</h2>
    </div>
      <div className='summary-list'>
        <h1>Stock Summaries</h1>
        {summaries.map((summary, index) => (
          <Summary 
            key={index}
            company={summary.company} 
            ticker={summary.ticker} 
            title={summary.title} 
            body={summary.body} 
            sentiment={summary.sentiment} 
            />
        ))}

      </div>
    </>
  )
}

export default App
