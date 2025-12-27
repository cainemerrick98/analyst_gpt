
function Event({ticker, title, company, date_, importance_for_price}){
    return (
        <div className="event">
            {ticker}: {title}
        </div>
    )
}

export default Event