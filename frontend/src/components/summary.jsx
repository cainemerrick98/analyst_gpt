
function Summary({company, ticker, title, body, sentiment}){
    return (
        <>
            <div style={{border:'1px solid white', marginBottom:'10px', padding:'5px', borderRadius:'10px'}}>
                <h2>{title}</h2>
                <h5>Sentiment: {sentiment}</h5>
                <p>{body}</p>   
            </div>
        </>
    )
}

export default Summary