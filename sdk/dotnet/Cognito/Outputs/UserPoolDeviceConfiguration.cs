// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolDeviceConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html#cfn-cognito-userpool-deviceconfiguration-challengerequiredonnewdevice
        /// </summary>
        public readonly bool? ChallengeRequiredOnNewDevice;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html#cfn-cognito-userpool-deviceconfiguration-deviceonlyrememberedonuserprompt
        /// </summary>
        public readonly bool? DeviceOnlyRememberedOnUserPrompt;

        [OutputConstructor]
        private UserPoolDeviceConfiguration(
            bool? ChallengeRequiredOnNewDevice,

            bool? DeviceOnlyRememberedOnUserPrompt)
        {
            this.ChallengeRequiredOnNewDevice = ChallengeRequiredOnNewDevice;
            this.DeviceOnlyRememberedOnUserPrompt = DeviceOnlyRememberedOnUserPrompt;
        }
    }
}