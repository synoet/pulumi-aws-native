// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ECR.Outputs
{

    /// <summary>
    /// The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.
    /// 
    /// By default, when no encryption configuration is set or the AES256 encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.
    /// 
    /// For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html
    /// </summary>
    [OutputType]
    public sealed class RepositoryEncryptionConfiguration
    {
        public readonly Pulumi.AwsNative.ECR.RepositoryEncryptionType EncryptionType;
        public readonly string? KmsKey;

        [OutputConstructor]
        private RepositoryEncryptionConfiguration(
            Pulumi.AwsNative.ECR.RepositoryEncryptionType encryptionType,

            string? kmsKey)
        {
            EncryptionType = encryptionType;
            KmsKey = kmsKey;
        }
    }
}
