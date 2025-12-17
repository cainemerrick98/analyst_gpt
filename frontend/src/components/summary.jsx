import './summary.css'

function Summary({company, ticker, title, body, sentiment}){
    return (
        <>
            <div className="summary">
                <h2>{title}</h2>
                <h5>Sentiment: {sentiment}</h5>
                <p>{body}</p>   
            </div>
        </>
    )
}

export default Summary