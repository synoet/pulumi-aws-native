// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds.Outputs
{

    [OutputType]
    public sealed class DbInstanceCertificateDetails
    {
        /// <summary>
        /// The CA identifier of the CA certificate used for the DB instance's server certificate.
        /// </summary>
        public readonly string? CaIdentifier;
        /// <summary>
        /// The expiration date of the DB instance’s server certificate.
        /// </summary>
        public readonly string? ValidTill;

        [OutputConstructor]
        private DbInstanceCertificateDetails(
            string? caIdentifier,

            string? validTill)
        {
            CaIdentifier = caIdentifier;
            ValidTill = validTill;
        }
    }
}
