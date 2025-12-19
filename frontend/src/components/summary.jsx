import './summary.css'
import { useState } from 'react'
import { parse } from 'marked'

function Summary({company, ticker, title, body, sentiment}){
    const [isCollapsed, setIsCollapsed] = useState(true)

    return (
        <div 
        className={isCollapsed ? "summary" : "summary expanded"}
        onClick={() => setIsCollapsed(!isCollapsed)}
        >
        <div style={{display:'flex', flexDirection:'horizontal', gap:'10px'}}>
            <div className={`circle ${sentiment}`}></div>
            <span>{company}  ({ticker})</span>
        </div>
            <h2>{title}</h2>
            <h5>Sentiment: {sentiment}</h5>
            <div dangerouslySetInnerHTML={{__html:parse(body)}}></div>
        </div>
    )
}

export default Summary