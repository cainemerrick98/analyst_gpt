import { useState, useMemo } from "react"
import './calendar.css'
import Event from "./event"
import EventModal from "./eventModal"

const currentMonthStart = new Date()
currentMonthStart.setDate(1)


function Calendar({events}){
    const [monthStart, setMonthStart] = useState(currentMonthStart)
    const [selectedEvent, setSelectedEvent] = useState(null)

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

    const changeMonthStart = (inc) => {
        setMonthStart(prev => {
            const d = new Date(prev)
            d.setMonth(d.getMonth() + inc)
            d.setDate(1)
            return d
        })
    }

    return (
        <>
            <div className="calendar-container">
                <div className="calendar-controls">
                    <div className="month-year-container">
                        <span>{monthStart.toLocaleString(undefined, {year:'numeric', month:'long'})}</span>
                    </div>
                    <div className="button-container">
                        <button onClick={() => changeMonthStart(-1)}>&lt;</button>
                        <button onClick={() => changeMonthStart(1)}>&gt;</button>
                    </div>
                    
                </div>
                <div className="calendar">
                    {Object.entries(daysAndEvents).map(([date, date_events]) => (
                        <div
                        key={new Date(date).toISOString()}
                        >
                            {new Date(date).getDate()}
                            {date_events.map((event, index) => (
                                <Event
                                    key={index}
                                    event={event}
                                    onClick={setSelectedEvent}
                                />
                            ))}
                        </div>
                    ))}
                </div>
            </div>
            {selectedEvent && (
                <EventModal
                    event={selectedEvent}
                    onClose={() => setSelectedEvent(null)}
                />
            )}
        </>
    )
}

export default Calendar  