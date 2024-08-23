import AdaptableCard from '@/components/shared/AdaptableCard'
import RichTextEditor from '@/components/shared/RichTextEditor'
import Input from '@/components/ui/Input'
import { FormItem } from '@/components/ui/Form'
import { Field, FormikErrors, FormikTouched, FieldProps } from 'formik'

type FormFieldsName = {
    shopName: string
    shopOwnername: string
}

type BasicInformationFields = {
    touched: FormikTouched<FormFieldsName>
    errors: FormikErrors<FormFieldsName>
}

const BasicInformationFields = (props: BasicInformationFields) => {
    const { touched, errors } = props

    return (
        <AdaptableCard divider className="mb-4">
            <h5>Basic Shop Information</h5>
            <p className="mb-6">Section to config basic Shop information</p>
            <FormItem
                label="Shop Name"
                invalid={(errors.shopName && touched.shopName) as boolean}
                errorMessage={errors.shopName}
            >
                <Field
                    type="text"
                    autoComplete="off"
                    name="shopName"
                    placeholder=" Shop Name"
                    component={Input}
                />
            </FormItem>
            <FormItem
                label="Shop Proprietor Name"
                invalid={(errors.shopOwnername && touched.shopOwnername) as boolean}
                errorMessage={errors.shopOwnername}
            >
                <Field
                    type="text"
                    autoComplete="off"
                    name="shopOwnername"
                    placeholder="Owner/Manager Name"
                    component={Input}
                />
            </FormItem>

        </AdaptableCard>
    )
}

export default BasicInformationFields
