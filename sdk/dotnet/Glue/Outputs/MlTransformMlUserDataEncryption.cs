// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Outputs
{

    [OutputType]
    public sealed class MlTransformMlUserDataEncryption
    {
        public readonly string? KmsKeyId;
        public readonly string MlUserDataEncryptionMode;

        [OutputConstructor]
        private MlTransformMlUserDataEncryption(
            string? kmsKeyId,

            string mlUserDataEncryptionMode)
        {
            KmsKeyId = kmsKeyId;
            MlUserDataEncryptionMode = mlUserDataEncryptionMode;
        }
    }
}
