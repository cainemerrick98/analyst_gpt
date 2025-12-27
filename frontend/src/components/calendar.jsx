import { useState, useMemo } from "react"
import './calendar.css'
import Event from "./event"

const currentMonthStart = new Date()
currentMonthStart.setDate(1)


function Calendar({events}){
    const [monthStart, setMonthStart] = useState(currentMonthStart)

    const daysAndEvents = useMemo(() => {
        const daysAndEvents = {}
        const date = new Date(monthStart)

        while (date.getMonth() === monthStart.getMonth()) {
            daysAndEvents[date] = []
            //this is not very efficient
            for(var event of events){
                if (date.toDateString() === new Date(event.date_).toDateString()){
                    daysAndEvents[date].push(event)
                }
            }
            date.setDate(date.getDate() + 1)
        }

        return daysAndEvents
    }, [monthStart])

    return (
        <>
            <div className="calendar-container">
                <div className="calendar-controls">
                    <h2>{monthStart.toLocaleString(undefined, {month:'long'})}</h2>
                </div>
                <div className="calendar">
                    {Object.entries(daysAndEvents).map((date, index, events) => (
                        <div
                        key={date.toISOString}
                        >
                            {date.getDate()}
                            {events.map((event) => (
                                <Event
                                    title={event.title}
                                    ticker={event.ticker}
                                    company={event.company}
                                    date_={event.date_}
                                    importance_for_price={event.importance_for_price}
                                />
                            ))}
                        </div>
                    ))}
                </div>
            </div>
        </>
    )
}

export default Calendar  