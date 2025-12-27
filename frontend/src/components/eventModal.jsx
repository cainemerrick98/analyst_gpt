import './eventModal.css'

function EventModal({ event, onClose }) {
  if (!event) return null

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <h3>{event.ticker}</h3>
        <p className="title">{event.title}</p>

        <div className="meta">
          <span>{event.company}</span>
          <span>{new Date(event.date_).toDateString()}</span>
        </div>

        <p className="importance">
          Price Impact: {event.importance_for_price}
        </p>

        <button onClick={onClose}>Close</button>
      </div>
    </div>
  )
}

export default EventModal
