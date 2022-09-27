import React from 'react'
import DownloadFile from '../components/core/downloadFile'
import FileForm from '../components/core/forms/fileForm'

type Props = {}

const Ote = (props: Props) => {
    const [filDbSwitch, setFilDbSwitch] = React.useState(false)

    // fillDbSwitch toggles between the file upload and database upload
    const handleFilDbSwitch = () => {
        setFilDbSwitch(!filDbSwitch)
    }

    return (
        <div>
            <button onClick={handleFilDbSwitch}>
                {!filDbSwitch ? 'Upload from file' : 'Upload from database'}
            </button>

            {filDbSwitch ? <FileForm /> : <div>Database upload</div>}
            <DownloadFile
                fileDbSwitch={filDbSwitch}
            />
        </div>
    )
}

export default Ote
