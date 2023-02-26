async function get() {    
    let word = window.location.search.split("=")[1]
    console.log(word)
    try {
        const res = await fetch('http://localhost:5000/contexts?word=' + word,
            {
                method: 'GET',
                withCredentials: true,
                crossorigin: true
            });
        const data = await res.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error(error);
    }    
}

async function sendPostRequest()
{
    number = await document.getElementById("defNumber").value;

    body = '{"context": "' + fullJson["context"] + '",  "context_id": "' + fullJson["context_id"] + '", "id": "' + number + '"}';
    
    console.log(JSON.parse(body))

    fetch("http://localhost:5000/annotation", {
        method: "POST",
        body: JSON.parse(body),
        headers: {
            "Content-type": "raw"
        }
    })
    .then((response) => response.json())
    .then((json) => console.log(json));;

    location.reload();
}
