// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class CoreDefinitionCoreDefinitionVersionArgs : Pulumi.ResourceArgs
    {
        [Input("cores", required: true)]
        private InputList<Inputs.CoreDefinitionCoreArgs>? _cores;
        public InputList<Inputs.CoreDefinitionCoreArgs> Cores
        {
            get => _cores ?? (_cores = new InputList<Inputs.CoreDefinitionCoreArgs>());
            set => _cores = value;
        }

        public CoreDefinitionCoreDefinitionVersionArgs()
        {
        }
    }
}
