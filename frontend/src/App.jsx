import './App.css'
import Summary from './components/summary'

function get_summaries(){
  return [
    {
      ticker: 'ASMLA',
      company: 'ASML',
      title: 'ASML Weekly Summary',
      body: 'The body of the summary',
      sentiment: 'Positive'
    },
    {
      ticker: 'ASMLA',
      company: 'ASML',
      title: 'ASML Weekly Summary',
      body: 'The body of the summary',
      sentiment: 'Positive'
    },

  ]
}

function App() {

  const summaries = get_summaries()

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
