import React from 'react'

const Card = ({car}) => {

    let {brand, model, year, price, color} = car
    
    return (
        <div className="bg-white shadow-md rounded-md p-5 m-4 flex-col">
            <div className="font-extrabold text-center border-b-2">{brand} {model}</div>
            <div>Year: {year}</div>
            <div>Price: <span className="font-semibold text- orange-600">{price}</span></div>
            <div>Color: {color}</div>
        </div>
    )
}

export default Card