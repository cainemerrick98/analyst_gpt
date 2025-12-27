const BASE_URL = import.meta.env.VITE_BASE_URL

export async function getStocks(){
    try{
        const res = await fetch(BASE_URL + 'stocks')
        if(res.ok){
            return await res.json()
        }else{
            return []
        }
    }catch{
        return []
    }
}

export async function getSummaries(){
    try {
        const res = await fetch(`${BASE_URL}summaries`);
        if(res.ok){
            return await res.json();
        }else{
            return []
        }
  } catch (err) {
    return [];
  }
}

export async function getEvents(){
    try {
        const res = await fetch(`${BASE_URL}events`);
        if(res.ok){
            return await res.json();
        }else{
            return []
        }
  } catch (err) {
    return [];
  }
}