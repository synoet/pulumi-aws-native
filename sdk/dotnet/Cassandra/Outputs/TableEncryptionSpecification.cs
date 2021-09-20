// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cassandra.Outputs
{

    /// <summary>
    /// Represents the settings used to enable server-side encryption
    /// </summary>
    [OutputType]
    public sealed class TableEncryptionSpecification
    {
        public readonly Pulumi.AwsNative.Cassandra.TableEncryptionType EncryptionType;
        public readonly string? KmsKeyIdentifier;

        [OutputConstructor]
        private TableEncryptionSpecification(
            Pulumi.AwsNative.Cassandra.TableEncryptionType encryptionType,

            string? kmsKeyIdentifier)
        {
            EncryptionType = encryptionType;
            KmsKeyIdentifier = kmsKeyIdentifier;
        }
    }
}
