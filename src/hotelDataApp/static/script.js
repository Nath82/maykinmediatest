// Async function to request and display hotel data
async function get_hotels(city) {
    var response = await fetch('http://127.0.0.1:8000/hotelsfromcity/'+city, {
        method: 'get',
    })
    var hotels = await response.json()

    // Now I display hotels data in index.html
    let title = document.getElementById('hoteltitle')
    title.textContent = "Here are the hotels that are in "+city
    let table = document.getElementById('hoteltable')
    table.style = "border:solid; margin:10px;"
    let row_1 = document.getElementById('tabletitle')
    let code = document.getElementById('code')
    let name = document.getElementById('name')
    code.textContent = "Code"
    name.textContent = "Name"

    // I clean the last table if you change the city
    while(table.firstChild){
        table.removeChild(table.firstChild)
    }
    row_1.appendChild(code)
    row_1.appendChild(name)
    table.appendChild(row_1)

    // for each hotel, I create a line with the code and the name of the hotel
    for (let i=0; i<hotels.length; i++) {
        let row_2 = document.createElement('tr')
        let hotel_code = document.createElement('td')
        let hotel_name = document.createElement('td')
        let hotel_code_link = document.createElement('a')
        let hotel_name_link = document.createElement('a')
        let text_code = document.createTextNode(hotels[i].hotel_code)
        let text_name = document.createTextNode(hotels[i].name)

        hotel_code_link.appendChild(text_code)
        hotel_name_link.appendChild(text_name)

        hotel_code_link.href = "singlehotel/"+hotels[i].hotel_code
        hotel_name_link.href = "singlehotel/"+hotels[i].hotel_code

        hotel_code.appendChild(hotel_code_link)
        hotel_name.appendChild(hotel_name_link)
        row_2.appendChild(hotel_code)
        row_2.appendChild(hotel_name)
        table.appendChild(row_2)
    }
}
