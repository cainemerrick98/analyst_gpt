import { useState, useMemo } from "react"
import './calendar.css'

const currentMonthStart = new Date()
currentMonthStart.setDate(1)


function Calendar(){
    const [monthStart, setMonthStart] = useState(currentMonthStart)

    const daysInMonth = useMemo(() => {
    const days = []
    const date = new Date(monthStart)

    while (date.getMonth() === monthStart.getMonth()) {
      days.push(new Date(date))
      date.setDate(date.getDate() + 1)
    }

    return days
  }, [monthStart])

    return (
        <>
            <div className="calendar-container">
                <div className="calendar-controls">
                    <h2>{monthStart.toLocaleString(undefined, {month:'long'})}</h2>
                </div>
                <div className="calendar">
                    {daysInMonth.map((date) => (
                        <div
                        key={date.toISOString}
                        >
                            {date.getDate()}
                        </div>
                    ))}
                </div>
            </div>
        </>
    )
}

export default Calendar  