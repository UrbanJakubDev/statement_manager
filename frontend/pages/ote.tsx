import React, { useEffect } from 'react'
import axios from 'axios'

// Importing the components
import FileForm from '../components/core/forms/fileForm'
import XmlGenForm from '../components/core/forms/dateForm'
import { useDownloadFile } from '../utils/useDownloadFile'

type Props = {}

interface IDateFormInput {
    year: number
    month: number
    unitsLimit: number
}

const Ote = (props: Props) => {
    // State

    // XmlGenForm submit handler
    const handleDateFormSubmit = (params: IDateFormInput) => {
        downloadFile(params)
    }
    // Utills
    const getFileName = () => {
        let date = new Date()
        return date.toISOString() + '.zip'
    }


    // TODO: Refactor to hook
    const makeDownload = (data: BlobPart) => {
        const url = window.URL.createObjectURL(new Blob([data]))
        const link = document.createElement('a')
        const fileName = getFileName()
        link.href = url
        link.setAttribute('download', fileName)
        document.body.appendChild(link)
        link.click()
    }

    // Axios calls functions
    const downloadFile = async (params: IDateFormInput) => {
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
            1. krok: Vygeneruj soubory pro dotaz na OTE
            <XmlGenForm onDateFormSubmit={handleDateFormSubmit} />

            2.krok: Nahrajte soubor do systému
            <FileForm apiURL="http://localhost:4200/ote/parse_xml_message/" />

            3.krok: Vygeneruj XLSX soubor
        </div>
    )
}

export default Ote
