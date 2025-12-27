import './event.css'

function Event({event, onClick}){
    return (
        <div className="event" onClick={() => onClick(event)}>
            {event.ticker}: {event.title}
        </div>
    )
}



export default Event