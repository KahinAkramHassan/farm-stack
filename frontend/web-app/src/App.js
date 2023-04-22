import Header from "./components/Header";
import Card from "./components/Card";
import {useEffect, useState, userEffect} from 'react'

function App() {

  const data = [
    {brand:"Fiat", color:"green", model:"500L", price:7000, "year":2020,"id":1},
    {brand:"Peugeot", color:"red", model:"5008", price:8000, "year":2018,"id":2},
    {brand:"Volkswagen", color:"white", model:"Golf 7", price:8500, "year":2019,"id":3},
    {brand:"Fiat", color:"green", model:"Tipo", price:10000, "year":2019,"id":4},
    {brand:"Kia", color:"black", model:"Ceed", price:6000, "year":2010,"id":5},
    {brand:"Volkswagen", color:"white", model:"Golf 7", price:8500, "year":2019,"id":15},
    {brand:"Fiat", color:"gray", model:"Ritmo", price:300, "year":1990,"id":21}
  ]

  const [budget, setBudget] = useState(4000)
  const onChangeHandler = event => setBudget(event.target.value)
  
  let [users, setUsers] = useState([])
  let [page, setPage] = useState(1)
  
  useEffect(()=>{
    
    fetch(`https://reqres.in/api/users?page=${page}`)
    .then(response=>response.json())
    .then(json=>setUsers(json['data']))
    
  },[page])




  return (
    <div className="App max-w-8xl mx-auto h-full">

      <Header/>
      <div class="flex flex-2">
        <div className="bg-gray-300 rounded-md p-3">
          <label htmlFor="budget">Budget:</label>
          <input type="number" onChange={onChangeHandler} id="budget" name="budget" min="300" max="12000" step="100" value={budget}></input>
          <div className="border-2 border-yellow-500 my-5 p-3">Your current budget is: <span className="">{budget}</span></div>
        </div>  

        <div class="inline-block h-[250px] min-h-[1em] w-0.5 self-stretch bg-neutral-100 opacity-100 dark:opacity-50"></div>
          <div className="grid grid-cols-8 my-3 gap-3">
            {data.map(
              (element)=>{
                
                return (
                  (element.price < budget ) && <Card key={element.id} car = {element} />
                  )
              }
            )}
          </div>
        </div>






      <div>
        <button className="border border-gray-500 rounded-md p-2 m-5" onClick={()=>{page===1?setPage(2):setPage(1)}}>Toggle users</button>
        <ul>
          {users&&users.map(el=>{
          return (
            <li key={el.id}>{el.email}</li>
            )
          })}
        </ul>
      </div>
    </div>
  );
}
export default App;