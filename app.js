const headerElement = document.querySelector("#header");
const hadithTextElement = document.querySelector("#hadith-text");
const bookElement = document.querySelector("#book");

const customButtonElement = document.querySelector("#customBtn");
const randomButtonElement = document.querySelector("#randomBtn");

const fetchJSON = async (hname, number, custom) => {
  let url = `https://random-hadith-generator.vercel.app/${hname}`;
  if (custom) {
    url += `/${number}`;
  }
  const response = await fetch(url, { mode: "cors" });
  const { data } = await response.json();
  return data;
};

const updateHadithData = ({ header, hadith_english, refno }) => {
  headerElement.innerHTML = header;
  hadithTextElement.innerHTML = hadith_english;
  bookElement.innerHTML = refno;
};

randomButtonElement.addEventListener("click", async (_) => {
  const hname = document.querySelector("#randomHadith").value;
  const hadithData = await fetchJSON(hname);
  updateHadithData(hadithData);
});

customButtonElement.addEventListener("click", async (_) => {
  const hname = document.querySelector("#customHadith").value;
  const number = document.querySelector("#customInput").value;
  const hadithData = await fetchJSON(hname, number, true);
  updateHadithData(hadithData);
});
