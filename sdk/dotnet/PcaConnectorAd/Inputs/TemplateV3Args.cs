// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Inputs
{

    public sealed class TemplateV3Args : global::Pulumi.ResourceArgs
    {
        [Input("certificateValidity", required: true)]
        public Input<Inputs.TemplateCertificateValidityArgs> CertificateValidity { get; set; } = null!;

        [Input("enrollmentFlags", required: true)]
        public Input<Inputs.TemplateEnrollmentFlagsV3Args> EnrollmentFlags { get; set; } = null!;

        [Input("extensions", required: true)]
        public Input<Inputs.TemplateExtensionsV3Args> Extensions { get; set; } = null!;

        [Input("generalFlags", required: true)]
        public Input<Inputs.TemplateGeneralFlagsV3Args> GeneralFlags { get; set; } = null!;

        [Input("hashAlgorithm", required: true)]
        public Input<Pulumi.AwsNative.PcaConnectorAd.TemplateHashAlgorithm> HashAlgorithm { get; set; } = null!;

        [Input("privateKeyAttributes", required: true)]
        public Input<Inputs.TemplatePrivateKeyAttributesV3Args> PrivateKeyAttributes { get; set; } = null!;

        [Input("privateKeyFlags", required: true)]
        public Input<Inputs.TemplatePrivateKeyFlagsV3Args> PrivateKeyFlags { get; set; } = null!;

        [Input("subjectNameFlags", required: true)]
        public Input<Inputs.TemplateSubjectNameFlagsV3Args> SubjectNameFlags { get; set; } = null!;

        [Input("supersededTemplates")]
        private InputList<string>? _supersededTemplates;
        public InputList<string> SupersededTemplates
        {
            get => _supersededTemplates ?? (_supersededTemplates = new InputList<string>());
            set => _supersededTemplates = value;
        }

        public TemplateV3Args()
        {
        }
        public static new TemplateV3Args Empty => new TemplateV3Args();
    }
}
