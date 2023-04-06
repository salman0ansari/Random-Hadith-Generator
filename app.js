const hadithHeader = document.querySelector("#header");
const hadithText = document.querySelector("#hadith-text");
const book = document.querySelector("#book");
const customBtn = document.querySelector("#customBtn");
const wrapper = document.querySelector("#wrapper");

const fetchHadithJSON = async (hname) => {
  const response = await fetch(
    `https://random-hadith-generator.vercel.app/${hname}`,
    { mode: "cors" }
  );
  const { data } = await response.json();
  return data;
};

const fetchCustom = async (hname, number) => {
  const response = await fetch(
    `https://random-hadith-generator.vercel.app/${hname}/${number}`,
    { mode: "cors" }
  );
  const { data } = await response.json();
  return data;
};

const loadHadithData = async (e) => {
  let hname;

  switch (e.target.id) {
    case "bukhari":
      hname = "bukhari";
      break;
    case "muslim":
      hname = "muslim";
      break;
    case "customBtn":
      const customHadith = document.querySelector("#customHadith").value;
      const number = document.querySelector("#customInput").value;
      if (customHadith === "bukhari") {
        hname = "bukhari";
        const hadithData = await fetchCustom("bukhari", number);

        const { header, hadith_english, refno } = hadithData;
        hadithHeader.innerHTML = header;
        hadithText.innerHTML = hadith_english;
        book.innerHTML = refno;
      } else if (customHadith === "muslim") {
        hname = "muslim";
        const hadithData = await fetchCustom("muslim", number);
        const { header, hadith_english, refno } = hadithData;
        hadithHeader.innerHTML = header;
        hadithText.innerHTML = hadith_english;
        book.innerHTML = refno;
      }
      return;
    default:
      return;
  }
  const hadithData = await fetchHadithJSON(hname);
  const { header, hadith_english, refno } = hadithData;
  hadithHeader.innerHTML = header;
  hadithText.innerHTML = hadith_english;
  book.innerHTML = refno;
};

const loadHadithOnButtonClick = async (e) => {
  await loadHadithData(e);
};

wrapper.addEventListener("click", loadHadithOnButtonClick);
