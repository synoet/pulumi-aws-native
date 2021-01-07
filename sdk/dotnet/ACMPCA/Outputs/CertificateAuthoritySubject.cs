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
    public sealed class CertificateAuthoritySubject
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-commonname
        /// </summary>
        public readonly string? CommonName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-country
        /// </summary>
        public readonly string? Country;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-distinguishednamequalifier
        /// </summary>
        public readonly string? DistinguishedNameQualifier;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-generationqualifier
        /// </summary>
        public readonly string? GenerationQualifier;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-givenname
        /// </summary>
        public readonly string? GivenName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-initials
        /// </summary>
        public readonly string? Initials;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-locality
        /// </summary>
        public readonly string? Locality;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organization
        /// </summary>
        public readonly string? Organization;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organizationalunit
        /// </summary>
        public readonly string? OrganizationalUnit;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-pseudonym
        /// </summary>
        public readonly string? Pseudonym;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-serialnumber
        /// </summary>
        public readonly string? SerialNumber;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-state
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-surname
        /// </summary>
        public readonly string? Surname;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-title
        /// </summary>
        public readonly string? Title;

        [OutputConstructor]
        private CertificateAuthoritySubject(
            string? CommonName,

            string? Country,

            string? DistinguishedNameQualifier,

            string? GenerationQualifier,

            string? GivenName,

            string? Initials,

            string? Locality,

            string? Organization,

            string? OrganizationalUnit,

            string? Pseudonym,

            string? SerialNumber,

            string? State,

            string? Surname,

            string? Title)
        {
            this.CommonName = CommonName;
            this.Country = Country;
            this.DistinguishedNameQualifier = DistinguishedNameQualifier;
            this.GenerationQualifier = GenerationQualifier;
            this.GivenName = GivenName;
            this.Initials = Initials;
            this.Locality = Locality;
            this.Organization = Organization;
            this.OrganizationalUnit = OrganizationalUnit;
            this.Pseudonym = Pseudonym;
            this.SerialNumber = SerialNumber;
            this.State = State;
            this.Surname = Surname;
            this.Title = Title;
        }
    }
}