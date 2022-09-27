import axios from 'axios'
import React from 'react'

type Props = {}

const FileForm = (props: Props) => {
    const [fileArray, setFileArray] = React.useState<File[]>([])
    const [isUploaded, setIsUploaded] = React.useState(false)
    const [uploadResponse, setUploadResponse] = React.useState({
        message: 'No file uploaded',
        filename: '',
    })

    // Utills
    const clearInput = () => {

		// Celar the input
        const input = document.getElementById('uploadFile')
        if (input) {
            input.value = ''
        }

		// Clear the file array
		setFileArray([])
    }

    // Hnadlers
    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            const files = Array.from(event.target.files)
            setFileArray(files)
        }
    }

    // Axios calls
    const handleFileUpload = (event: { preventDefault: () => void }) => {
        event.preventDefault()
        if (fileArray.length > 0) {
            const formData = new FormData()
            fileArray.forEach((file) => {
                formData.append('file', file)
            })
            axios
                .post('http://localhost:4200/example/upload/', formData)
                .then((res) => {
                    setUploadResponse(res.data)
                    setIsUploaded(true)
                })
                .catch((err) => {
                    console.log(err)
                })
        }

        // Clear the input
        clearInput()
    }

    // Render
    return (
        <div>
            <span>Formulář</span>
            <form>
                <input
                    id="uploadFile"
                    type="file"
                    multiple
                    accept=".xls,.xlsx,.csv"
                    onChange={handleFileChange}
                />
                <button type="submit" onClick={handleFileUpload}>
                    Upload
                </button>
            </form>
            <span>File List</span>
            <div>
                {fileArray.map((file, index) => {
                    return (
                        <div key={index}>
                            {file.name +
                                ' ' +
                                index +
                                ' of ' +
                                fileArray.length}
                        </div>
                    )
                })}
            </div>
            <span>Server response</span>
            <div>{uploadResponse.message}</div>
        </div>
    )
}

export default FileForm
