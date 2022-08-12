let selectCount = 0
class CustomSelect {
    
    constructor(originalSelect) {
      this.originalSelect = originalSelect;
      this.customSelect = document.createElement("div");
      this.customSelect.classList.add("select");
  
      this.originalSelect.querySelectorAll("option").forEach((optionElement) => {
        const itemElement = document.createElement("div");
  
        itemElement.classList.add("select__item");
        itemElement.textContent = optionElement.textContent;
        this.customSelect.appendChild(itemElement);
  
        if (optionElement.selected) {
          this._select(itemElement);
        }
  
        itemElement.addEventListener("click", () => {
          if (
            this.originalSelect.multiple &&
            itemElement.classList.contains("select__item--selected")
          ) {
            this._deselect(itemElement);
          } else {
            this._select(itemElement);
          }
        });
      });
  
      this.originalSelect.insertAdjacentElement("afterend", this.customSelect);
      this.originalSelect.style.display = "none";
    }
  
    _select(itemElement) {

      if (selectCount < 14) {
          selectCount = selectCount +1
          document.getElementById("selected-figure").innerHTML = selectCount
          
          const index = Array.from(this.customSelect.children).indexOf(itemElement);
      
          if (!this.originalSelect.multiple) {
            this.customSelect.querySelectorAll(".select__item").forEach((el) => {
              el.classList.remove("select__item--selected");
            });
          }
    
          this.originalSelect.querySelectorAll("option")[index].selected = true;
    
          itemElement.classList.add("select__item--selected");
      }
      if (selectCount == 14) {
        document.getElementById("submit").style.display = "block"
      } else {
        document.getElementById("submit").style.display = "none"
      }
    }
  
    _deselect(itemElement) {
      selectCount = selectCount -1
      if (selectCount == 14) {
        document.getElementById("submit").style.display = "block"
      } else {
        document.getElementById("submit").style.display = "none"
      }
      const index = Array.from(this.customSelect.children).indexOf(itemElement);
      
      this.originalSelect.querySelectorAll("option")[index].selected = false;

      document.getElementById("selected-figure").innerHTML = selectCount
      
      itemElement.classList.remove("select__item--selected");
    }
  }
  
  document.querySelectorAll(".custom-select").forEach((selectElement) => {
    new CustomSelect(selectElement);
  });