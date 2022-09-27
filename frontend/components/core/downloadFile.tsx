import axios from 'axios'
import React from 'react'

type Props = {
    fileDbSwitch: boolean,
}

const DownloadFile = (props: Props) => {
    // State
    const [xmlGenParams, setXmlGenParams] = React.useState({
        year: '',
        month: ''
    })

    // Utills
    const generateDownloadFileName = () => {
        let date = new Date()
        let str_date = date.toISOString()
        return str_date
    }

    const makeDownload = (response: { data: BlobPart }) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        const fileName = generateDownloadFileName() + '.xml'
        link.href = url
        link.setAttribute('download', fileName)
        document.body.appendChild(link)
        link.click()
    }

    // Hnadlers
    const handleGenerateXML = async () => {

    }

    // Axios calls
    const downloadDataDb = async () => {
        const response = await axios
            .get('http://localhost:4200/ote/make_xml_message/', {
                responseType: 'blob',
            })
            .then((response) => {
                makeDownload(response)
            })
    }

    const downloadDataFile = async () => {
        const response = await axios
            .get('http://localhost:4200/ote/make_xml_message/', {
                responseType: 'blob',
            })
            .then((response) => {
                makeDownload(response)
            })
    }

    // Render

    return (
        <div>
            <h3 onClick={downloadDataDb}>Generate XML</h3>
        </div>
    )
}

export default DownloadFile
