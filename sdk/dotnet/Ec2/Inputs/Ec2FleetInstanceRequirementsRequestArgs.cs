// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    public sealed class Ec2FleetInstanceRequirementsRequestArgs : global::Pulumi.ResourceArgs
    {
        [Input("acceleratorCount")]
        public Input<Inputs.Ec2FleetAcceleratorCountRequestArgs>? AcceleratorCount { get; set; }

        [Input("acceleratorManufacturers")]
        private InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorManufacturersItem>? _acceleratorManufacturers;
        public InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorManufacturersItem> AcceleratorManufacturers
        {
            get => _acceleratorManufacturers ?? (_acceleratorManufacturers = new InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorManufacturersItem>());
            set => _acceleratorManufacturers = value;
        }

        [Input("acceleratorNames")]
        private InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorNamesItem>? _acceleratorNames;
        public InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorNamesItem> AcceleratorNames
        {
            get => _acceleratorNames ?? (_acceleratorNames = new InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorNamesItem>());
            set => _acceleratorNames = value;
        }

        [Input("acceleratorTotalMemoryMiB")]
        public Input<Inputs.Ec2FleetAcceleratorTotalMemoryMiBRequestArgs>? AcceleratorTotalMemoryMiB { get; set; }

        [Input("acceleratorTypes")]
        private InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorTypesItem>? _acceleratorTypes;
        public InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorTypesItem> AcceleratorTypes
        {
            get => _acceleratorTypes ?? (_acceleratorTypes = new InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestAcceleratorTypesItem>());
            set => _acceleratorTypes = value;
        }

        [Input("allowedInstanceTypes")]
        private InputList<string>? _allowedInstanceTypes;
        public InputList<string> AllowedInstanceTypes
        {
            get => _allowedInstanceTypes ?? (_allowedInstanceTypes = new InputList<string>());
            set => _allowedInstanceTypes = value;
        }

        [Input("bareMetal")]
        public Input<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestBareMetal>? BareMetal { get; set; }

        [Input("baselineEbsBandwidthMbps")]
        public Input<Inputs.Ec2FleetBaselineEbsBandwidthMbpsRequestArgs>? BaselineEbsBandwidthMbps { get; set; }

        [Input("burstablePerformance")]
        public Input<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestBurstablePerformance>? BurstablePerformance { get; set; }

        [Input("cpuManufacturers")]
        private InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestCpuManufacturersItem>? _cpuManufacturers;
        public InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestCpuManufacturersItem> CpuManufacturers
        {
            get => _cpuManufacturers ?? (_cpuManufacturers = new InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestCpuManufacturersItem>());
            set => _cpuManufacturers = value;
        }

        [Input("excludedInstanceTypes")]
        private InputList<string>? _excludedInstanceTypes;
        public InputList<string> ExcludedInstanceTypes
        {
            get => _excludedInstanceTypes ?? (_excludedInstanceTypes = new InputList<string>());
            set => _excludedInstanceTypes = value;
        }

        [Input("instanceGenerations")]
        private InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestInstanceGenerationsItem>? _instanceGenerations;
        public InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestInstanceGenerationsItem> InstanceGenerations
        {
            get => _instanceGenerations ?? (_instanceGenerations = new InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestInstanceGenerationsItem>());
            set => _instanceGenerations = value;
        }

        [Input("localStorage")]
        public Input<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestLocalStorage>? LocalStorage { get; set; }

        [Input("localStorageTypes")]
        private InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestLocalStorageTypesItem>? _localStorageTypes;
        public InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestLocalStorageTypesItem> LocalStorageTypes
        {
            get => _localStorageTypes ?? (_localStorageTypes = new InputList<Pulumi.AwsNative.Ec2.Ec2FleetInstanceRequirementsRequestLocalStorageTypesItem>());
            set => _localStorageTypes = value;
        }

        [Input("memoryGiBPerVCpu")]
        public Input<Inputs.Ec2FleetMemoryGiBPerVCpuRequestArgs>? MemoryGiBPerVCpu { get; set; }

        [Input("memoryMiB")]
        public Input<Inputs.Ec2FleetMemoryMiBRequestArgs>? MemoryMiB { get; set; }

        [Input("networkBandwidthGbps")]
        public Input<Inputs.Ec2FleetNetworkBandwidthGbpsRequestArgs>? NetworkBandwidthGbps { get; set; }

        [Input("networkInterfaceCount")]
        public Input<Inputs.Ec2FleetNetworkInterfaceCountRequestArgs>? NetworkInterfaceCount { get; set; }

        [Input("onDemandMaxPricePercentageOverLowestPrice")]
        public Input<int>? OnDemandMaxPricePercentageOverLowestPrice { get; set; }

        [Input("requireHibernateSupport")]
        public Input<bool>? RequireHibernateSupport { get; set; }

        [Input("spotMaxPricePercentageOverLowestPrice")]
        public Input<int>? SpotMaxPricePercentageOverLowestPrice { get; set; }

        [Input("totalLocalStorageGb")]
        public Input<Inputs.Ec2FleetTotalLocalStorageGbRequestArgs>? TotalLocalStorageGb { get; set; }

        [Input("vCpuCount")]
        public Input<Inputs.Ec2FleetVCpuCountRangeRequestArgs>? VCpuCount { get; set; }

        public Ec2FleetInstanceRequirementsRequestArgs()
        {
        }
        public static new Ec2FleetInstanceRequirementsRequestArgs Empty => new Ec2FleetInstanceRequirementsRequestArgs();
    }
}
