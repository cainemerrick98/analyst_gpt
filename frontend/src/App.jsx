import './App.css'
import Summary from './components/summary'
import Calendar from './components/calendar';
import { getStocks, getSummaries, getEvents } from './services/api'
import { useEffect, useState } from 'react';


function App() {
  const [summaries, setSummaries] = useState([]);
  const [stocks, setStocks] = useState([]);
  const [events, setEvents] = useState([]);
  const [selectedTab, setSelectedTab] = useState('Summaries')

  useEffect(() => {
    async function loadData() {
      const summariesData = await getSummaries();
      const stocksData = await getStocks();
      const eventsData = await getEvents();

      setSummaries(summariesData);
      setStocks(stocksData);
      setEvents(eventsData)
    }

    loadData();
  }, []);


  return (
    <>
    <div className='header'>
      <h2>My Stock Tracker</h2>
    </div>
    <div className='tabs'>
      <span 
        className={selectedTab == 'Summaries' ? 'selected' : ''}
        onClick={() => setSelectedTab('Summaries')}
      >Summaries</span>
      <span
        className={selectedTab == 'Calendar' ? 'selected' : ''}
        onClick={() => setSelectedTab('Calendar')}
      >Calendar</span>
      <span
        className={selectedTab == 'Stocks' ? 'selected' : ''}
        onClick={() => setSelectedTab('Stocks')}
      >Stocks</span>
    </div>
    <div 
      hidden={selectedTab == 'Summaries' ? false : true}
      className='summary-list'>
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
    <div 
      hidden={selectedTab == 'Calendar' ? false : true}
      className='calendar-container'>
        <Calendar/>
    </div>
    <div 
      hidden={selectedTab == 'Stocks' ? false : true}
      className='stocks-list'>
        Stocks
    </div>
    </>
  )
}

export default App
