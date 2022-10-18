import React from 'react'
import { useForm } from 'react-hook-form'

type Props = {
    // Callback function to return the selected year and month to the parent component
    onDateFormSubmit: (params: { year: number; month: number, unitsLimit: number }) => void
}

const DateForm = (props: Props) => {
    const { register, handleSubmit } = useForm()

    const getActualMonth = () => {
        let month = new Date().getMonth().toString()
        return month.length === 1 ? '0' + month : month
    }


    // Form submit handler
    const onSubmit = (data: any) => {
        props.onDateFormSubmit(data)
    }

    const onErrors = (errors: any) => console.error(errors)

    return (
        <div className="component">
            <h2>Date picker</h2>
            <form onSubmit={handleSubmit(onSubmit, onErrors)}>
                <label htmlFor="year">Year</label>
                <select id="year" {...register('year')} defaultValue={new Date().getFullYear()}>
                    <option value="2022">2022</option>
                    <option value="2023">2023</option>
                    <option value="2024">2024</option>
                </select>
                <label htmlFor="month">Month</label>
                <select id="month" {...register('month')} defaultValue={getActualMonth()}>
                    <option value="01">01</option>
                    <option value="02">02</option>
                    <option value="03">03</option>
                    <option value="04">04</option>
                    <option value="05">05</option>
                    <option value="06">06</option>
                    <option value="07">07</option>
                    <option value="08">08</option>
                    <option value="09">09</option>
                    <option value="10">10</option>
                    <option value="11">11</option>
                    <option value="12">12</option>
                </select>

                <label htmlFor="units-limit">Units limit</label>
                <select id="units-limit" {...register('units-limit')}>
                    <option value="50">50</option>
                    <option value="40">40</option>
                    <option value="30">30</option>
                    <option value="20">20</option>
                </select>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default DateForm
