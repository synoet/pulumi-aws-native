// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ACMPCA.Outputs
{

    [OutputType]
    public sealed class CertificateValidity
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-type
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-value
        /// </summary>
        public readonly int Value;

        [OutputConstructor]
        private CertificateValidity(
            string Type,

            int Value)
        {
            this.Type = Type;
            this.Value = Value;
        }
    }
}