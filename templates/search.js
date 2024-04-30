const inpSearch = document.querySelector("#search-input");

inpSearch.addEventListener('input', onSearchChange)

let filmNames = []

async function getAllMatchedDesciption(searchText) {
  let requestedUrl = `http://127.0.0.1:4000/api/netflix/films/${searchText}`
  const filmResponses = await fetch(requestedUrl);
  const films = await filmResponses.json();
  filmNames = films.map((item) => {
    return item.description;
  })
}


function onSearchChange() {
  removeDropdown();
  const searchText = inpSearch.value.toLowerCase();
  const films = []
  getAllMatchedDesciption(searchText);
  filmNames.forEach((film) => {
    films.push(film);

  })
  createDropdown(films, searchText);
}


function createDropdown(items, searchText) {
  const ulElem = document.createElement('ul');
  ulElem.className = "list-result";
  ulElem.id = "list-result";

  items.forEach((item) => {
    const liElem = document.createElement('li');
    const butElem = document.createElement('button');
    butElem.id = "button-value";
    let replacedText = "<strong>" + searchText + "</strong>";
    butElem.innerHTML = item.replace(searchText, replacedText);
    butElem.addEventListener('click', onSearchTermClick)
    liElem.appendChild(butElem);
    ulElem.appendChild(liElem);
  })

  document.querySelector("#autocomplete-wrapper").appendChild(ulElem);
}

function removeDropdown() {
  const dropdown = document.querySelector('#list-result');
  if (dropdown) {
    dropdown.remove()
  }
}

function onSearchTermClick(e) {
  const searchTerm = e.target;
  inpSearch.value = searchTerm.innerHTML;
  removeDropdown();
}
