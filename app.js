let header = document.querySelector('#header');
let hadith = document.querySelector('#hadith-text');
let book = document.getElementById('book')
const wrapper = document.getElementById('wrapper');

// Request Hadith Data from API
async function fetchHadithJSON(hname) {
  const response = await fetch(`https://random-hadith-generator.vercel.app/${hname}`, {
    mode: "cors"
  });
  const hadith = await response.json();
  // book.innerHTML = 
  console.log(book.value)
  
  return hadith;
}

// Load Hadith Data from API
async function loadHadith(e) {
  if(e.target.id === "bukhari") {
        hname = 'bukhari'
    } else if (e.target.id === "muslim") {
        hname = 'muslim'
    }
    const {data} =  await fetchHadithJSON(hname)
    header.innerHTML = data.header;
    hadith.innerHTML = data.hadith_english;
    book.innerHTML = data.refno
}

// Get a random hadith when button is clicked
async function loadHadithOnButtonClick(e) {
    loadHadith(e)
}

wrapper.addEventListener('click', loadHadithOnButtonClick);
