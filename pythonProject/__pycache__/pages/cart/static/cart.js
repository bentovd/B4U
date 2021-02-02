function cartFilter(id){ //create filter in page
  if(id=="cart-quantity"){
    document.getElementById(id).innerHTML =`
    <label for="quantity">כמות:</label>
        <select id="quantity" name="quantity" style="display:block;">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
        </select>

    `
  }
  if(id=="cart-size"){
    document.getElementById(id).innerHTML =`
    <label for="size">מידה:</label>
        <select id="size" name="size" style="display:block;">
            <option value="XS">XS</option>
            <option value="S">S</option>
            <option value="M">M</option>
            <option value="L">L</option>
        </select>

    `
  }
  if(id=="cart-color"){
    document.getElementById(id).innerHTML =`
    <label for="color">צבע:</label>
    <select id="color" name="color" style="display:block;">
        <option value="Red">אדום</option>
        <option value="Yellow">צהוב</option>
        <option value="Blue">כחול</option>
        <option value="Green">ירוק</option>
    </select>

    `
  }


}