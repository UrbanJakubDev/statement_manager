import React, { useEffect } from 'react'
import FileForm from '../components/core/forms/fileForm'
import XmlGenForm from '../components/core/forms/dateForm'
import axios from 'axios'

type Props = {}

interface IDateFormInput {
    year: number
    month: number
}

const Ote = (props: Props) => {
    // State

    // XmlGenForm submit handler
    const handleDateFormSubmit = (params: IDateFormInput) => {
        downloadData(params)
    }
    // Utills
    const generateDownloadFileName = () => {
        let date = new Date()
        let str_date = date.toISOString()
        return str_date
    }

    const makeDownload = (data: BlobPart) => {
        const url = window.URL.createObjectURL(new Blob([data]))
        const link = document.createElement('a')
        const fileName = generateDownloadFileName() + '.zip'
        link.href = url
        link.setAttribute('download', fileName)
        document.body.appendChild(link)
        link.click()
    }

    // Axios calls functions
    const downloadData = async (params: IDateFormInput) => {
        const response = await axios
            .get('http://localhost:4200/ote/make_xml_message/', {
                responseType: 'blob',
                params: params,
            })
            .then((response) => {
                makeDownload(response.data)
            })
    }

    return (
        <div>
            <XmlGenForm onDateFormSubmit={handleDateFormSubmit} />
        </div>
    )
}

export default Ote
