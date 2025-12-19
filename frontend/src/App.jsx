import './App.css'
import Summary from './components/summary'

function get_summaries() {
  return [
    {
      ticker: 'ASML',
      company: 'ASML Holding',
      title: 'ASML Weekly Market Summary',
      body: `
ASML shares moved higher this week following strong demand signals from the semiconductor sector.

Management reiterated confidence in long-term EUV adoption, citing increased investment from major foundries in both the U.S. and Asia.

Key highlights:
- Strong backlog visibility through 2026
- Continued margin expansion driven by service revenue
- Increased geopolitical diversification of customers

Risks remain, particularly around export restrictions and macroeconomic uncertainty, but overall sentiment remains constructive.

Conclusion:
ASML continues to be viewed as a core long-term holding within the semiconductor equipment space.
      `,
      sentiment: 'Positive'
    },

    {
      ticker: 'NVDA',
      company: 'NVIDIA',
      title: 'NVIDIA Weekly Market Summary',
      body: `
NVIDIA experienced heightened volatility this week as investors reacted to mixed signals around AI infrastructure spending.

While demand for data center GPUs remains robust, some customers are beginning to optimize existing capacity rather than aggressively expand.

Notable developments:
- AI revenue growth remains strong quarter-over-quarter
- Gross margins stabilized after recent declines
- Competition in custom silicon continues to increase

Overall, the market appears to be reassessing expectations rather than abandoning the long-term AI thesis.
      `,
      sentiment: 'Neutral'
    }
  ];
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
