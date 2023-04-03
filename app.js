let header = document.querySelector("#header");
let hadith = document.querySelector("#hadith-text");
let book = document.getElementById("book");
let customBtn = document.getElementById("customBtn ");
const wrapper = document.getElementById("wrapper");

// Request Hadith Data from API
async function fetchHadithJSON(hname) {
  const response = await fetch(
    `https://random-hadith-generator.vercel.app/${hname}`,
    {
      mode: "cors",
    }
  );
  const hadith = await response.json();
  return hadith;
}

async function fetchCustom(hname, number) {
  const response = await fetch(
    `https://random-hadith-generator.vercel.app/${hname}/${number}`,
    {
      mode: "cors",
    }
  );
  const hadith = await response.json();
  return hadith;
}

// Load Hadith Data from API
async function loadHadith(e) {
  if (e.target.id === "bukhari") {
    hname = "bukhari";
  } else if (e.target.id === "muslim") {
    hname = "muslim";
  } else if (e.target.id === "customBtn") {
    console.log("customBtn");
    let customHadith = document.getElementById("customHadith").value;
    let number = document.getElementById("customInput").value;
    if (customHadith === "bukhari") {
      hname = "bukhari";
      const { data } = await fetchCustom("bukhari", number);
      header.innerHTML = data.header;
      hadith.innerHTML = data.hadith_english;
      book.innerHTML = data.refno;
      return;
    } else if (customHadith === "muslim") {
      hname = "muslim";
      const { data } = await fetchCustom("muslim", number);
      header.innerHTML = data.header;
      hadith.innerHTML = data.hadith_english;
      book.innerHTML = data.refno;
    }
    return;
  }

  const { data } = await fetchHadithJSON(hname);
  header.innerHTML = data.header;
  hadith.innerHTML = data.hadith_english;
  book.innerHTML = data.refno;
}

// Get a random hadith when button is clicked
async function loadHadithOnButtonClick(e) {
  loadHadith(e);
}

wrapper.addEventListener("click", loadHadithOnButtonClick);
