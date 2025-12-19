export async function getStocks(){
    var stocks = await fetch(
        process.env.BASE_URL + 'stocks'
    )
    return stocks
}

export async function getSummaries(){
    var summaries = await fetch(
        process.env.BASE_URL + 'summaries'
    )
    return summaries
}