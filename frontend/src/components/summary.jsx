import './summary.css'
import { useState } from 'react'
import { marked } from 'marked'

const renderer = new marked.Renderer()
renderer.link = ({ href, title, text }) => {
  const t = title ? ` title="${title}"` : ''
  return `<a href="${href}" target="_blank" rel="noopener noreferrer"${t}>${text}</a>`
}
marked.setOptions({ renderer })

function Summary({company, ticker, title, body, sentiment, key_points, date_created}){
    const [isCollapsed, setIsCollapsed] = useState(true)

    return (
        <div 
        className={isCollapsed ? "summary" : "summary expanded"}
        onClick={() => setIsCollapsed(!isCollapsed)}
        >
        <div style={{display:'flex', flexDirection:'row', justifyContent:'space-between'}}>
            <div style={{display:'flex', flexDirection:'row', gap:'10px'}} >
                <div className={`circle ${sentiment}`}></div>
                <span>{company}  ({ticker})</span>
            </div>
            <div>{date_created}</div>
        </div>
            <h2>{title}</h2>
            <h5>Sentiment: {sentiment}</h5>
            {isCollapsed ? 
                <ul>
                    {key_points.split(`','`).map((kp, index) => (
                        <li key={index}>{kp}</li>
                    ))}
                </ul>
                :
                <div dangerouslySetInnerHTML={{__html:marked.parse(body)}}></div>
            }
        </div>
    )
}

export default Summary