// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.HealthLake.Outputs
{

    /// <summary>
    /// The customer-managed-key (CMK) used when creating a Data Store. If a customer owned key is not specified, an AWS owned key will be used for encryption.
    /// </summary>
    [OutputType]
    public sealed class FHIRDatastoreKmsEncryptionConfig
    {
        /// <summary>
        /// The type of customer-managed-key (CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.
        /// </summary>
        public readonly Pulumi.AwsNative.HealthLake.FHIRDatastoreKmsEncryptionConfigCmkType CmkType;
        /// <summary>
        /// The KMS encryption key id/alias used to encrypt the Data Store contents at rest.
        /// </summary>
        public readonly string? KmsKeyId;

        [OutputConstructor]
        private FHIRDatastoreKmsEncryptionConfig(
            Pulumi.AwsNative.HealthLake.FHIRDatastoreKmsEncryptionConfigCmkType cmkType,

            string? kmsKeyId)
        {
            CmkType = cmkType;
            KmsKeyId = kmsKeyId;
        }
    }
}
