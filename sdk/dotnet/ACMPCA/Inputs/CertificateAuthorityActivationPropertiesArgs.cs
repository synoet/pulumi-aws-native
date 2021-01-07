// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ACMPCA.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html
    /// </summary>
    public sealed class CertificateAuthorityActivationPropertiesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificate
        /// </summary>
        [Input("Certificate", required: true)]
        public Input<string> Certificate { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificateauthorityarn
        /// </summary>
        [Input("CertificateAuthorityArn", required: true)]
        public Input<string> CertificateAuthorityArn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificatechain
        /// </summary>
        [Input("CertificateChain")]
        public Input<string>? CertificateChain { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-status
        /// </summary>
        [Input("Status")]
        public Input<string>? Status { get; set; }

        public CertificateAuthorityActivationPropertiesArgs()
        {
        }
    }
}