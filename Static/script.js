async function fetchAPI(url, method="GET", data=null){

    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json"
        }
    };

    if(data){
        options.body = JSON.stringify(data);
    }

    const res = await fetch(url, options);

    if(!res.ok){
        throw new Error("API request failed");
    }

    return await res.json();
}